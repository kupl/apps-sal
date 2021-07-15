N = int(input())
S = list(map(str, input().split()))

candy_list = ['P', 'W', 'G', 'Y']
answer = 0
for i in range(4):
    if candy_list[i] in S:
        answer += 1

if answer == 3:
    print('Three')
if answer == 4:
    print('Four')
