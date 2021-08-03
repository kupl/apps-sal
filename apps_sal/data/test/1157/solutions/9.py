N = int(input())
nums = list(map(int, input().split()))

# (neg, pos)
tot = (1, 0) if nums[0] < 0 else (0, 1)

runTot = tot
for i in range(1, N):
    if nums[i] > 0:
        tot = (tot[0], tot[1] + 1)
    else:
        tot = (tot[1] + 1, tot[0])
    runTot = (runTot[0] + tot[0], runTot[1] + tot[1])

print(runTot[0], runTot[1])
