N = int(input())
num_list = list(map(int, input().split()))
ANS = 0
tall = 0
pre = 0
for i in range(N):
    if tall > num_list[i]:
        pre = tall - num_list[i]
        ANS += pre
        tall = num_list[i] + pre
    else:
        tall = num_list[i]
print(ANS)
