n = int(input())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
answer1 = 0
answer2 = 0
for i in range(n):
    answer1 |= s1[i]
    answer2 |= s2[i]
print(answer1 + answer2)
