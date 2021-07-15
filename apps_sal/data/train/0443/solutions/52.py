class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        while len(rating) > 0:
            r = rating.pop(0)
            # print(r)
            counter += countDown(rating, r, 1)
            counter += countUp(rating, r, 1)
        return counter
    
def countUp(rating, value, num_in_team):
    # print(f'countUp({rating}, {value}, {num_in_team}):')
    if len(rating) == 0:
        return 0
    counter = 0
    for i, num in enumerate(rating):
        if  num > value and num_in_team == 2:
            # print(f'{num} is larger than {value} and tahts a team')
            counter += 1
        elif num > value:
            # print(f'{num} is larger than {value}')
            counter += countUp(rating[i:], num, 2)
    # print(f'returning counter with value {counter}')
    return counter

def countDown(rating, value, num_in_team):
    # print(f'countDown({rating}, {value}, {num_in_team}):')
    if len(rating) == 0:
        return 0
    counter = 0
    for i, num in enumerate(rating):
        if  num < value and num_in_team == 2:
            # print(f'{num} is smaller than {value} and tahts a team')
            counter += 1
        elif num < value:
            counter += countDown(rating[i:], num, 2)
    # print(f'returning counter with value {counter}')
    return counter

