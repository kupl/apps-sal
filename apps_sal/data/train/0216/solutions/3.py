class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = 1
        waitingFor = defaultdict(int)
        croak = 'croak'
        croakDict= {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        
        # waitingFor['c'] = 0
        for char in croakOfFrogs:
            if char == 'c':
                if waitingFor[char] != 0 and ans <= waitingFor[char]:
                    ans += 1
                waitingFor[char] += 1
                waitingFor[croak[croakDict[char]+1]] += 1
            else:
                if waitingFor[char] == 0:
                    return -1
                waitingFor[char] -= 1
                if char != 'k':
                    waitingFor[croak[croakDict[char]+1]] += 1
                else:
                    waitingFor['c'] -= 1
        # print(waitingFor)
        for char in waitingFor:
            if waitingFor[char] != 0:
                return -1
        return ans
