N = int(input())
ppl = 0
for i in range(N):
    tmp = input().split(" ")
    ppl += int(tmp[1]) - int(tmp[0]) + 1

print(ppl)
