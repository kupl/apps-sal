class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        j = len(people) - 1
        i = 0
        people = sorted(people)
        # since we could max have two people on a boat so we need to add have two ###pointers
        print(people)
        count = 0
        while(i <= j):
            count = count + 1
            if people[j] + people[i] <= limit:
                i = i + 1
                j = j - 1
            else:
                j = j - 1
        return(count)
