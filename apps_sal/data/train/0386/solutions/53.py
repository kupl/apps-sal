"""
Dynamic programing with recursion?

Base case is five. 

[1,1,1,1,1]

a =1 e=2 i=4 o=2 u=1

a,e
e,a | e,i
i,a | i,e | i,u, |i,o
o,i | o,u
u,a

a = 2, e = 5, i = 10 ,o = 5, u =1



Each round, you are calculating the number of permutations a letter has if you were to stick it in front.

for instance: i


for 3 letters:
i: used the previous 
a,e
e,a | e,i
o,i | o,u
u,a

for a total of 6 additional permutations. 



"""


class Solution:

    def countVowelPermutation(self, n: int) -> int:
        prev_count = [1, 2, 4, 2, 1]
        if n == 1:
            return 5
        if n == 2:
            return sum(prev_count)
        for i in range(3, n + 1):
            current_count = [0] * 5
            current_count[0] = prev_count[1]
            current_count[1] = prev_count[0] + prev_count[2]
            current_count[2] = prev_count[0] + prev_count[1] + prev_count[3] + prev_count[4]
            current_count[3] = prev_count[2] + prev_count[4]
            current_count[4] = prev_count[0]
            prev_count = current_count
        return sum(current_count) % (10 ** 9 + 7)
