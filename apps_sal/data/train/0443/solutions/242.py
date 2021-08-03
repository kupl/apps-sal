def findmyTeams(myrating: List[int], member_list: List[int], current_member: int) -> int:
    my_new_member_list = member_list.copy()
    if(len(member_list) == 3):
        # print(member_list)
        return 1
    elif(len(myrating) == 0):
        return 0

    score = 0
    for a in range(len(myrating)):
        if(myrating[a] > current_member):
            #print(myrating[a], current_member)
            my_new_member_list.append(myrating[a])
            score += findmyTeams(myrating[a:], my_new_member_list, myrating[a])
            my_new_member_list.pop()

    return score


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # We will iterate through the list from left to right first.
        # So that means we will have two for loops
        answer = 0
        for i in range(len(rating)):
            answer += findmyTeams(rating[i:], [rating[i]], rating[i])

        # print(\"Normal:\", answer)

        rating.reverse()
        for i in range(len(rating)):
            answer += findmyTeams(rating[i:], [rating[i]], rating[i])

        # print(\"Reversed: \", answer)

        return(answer)
