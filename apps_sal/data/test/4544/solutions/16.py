input()
B = [0] * 10**5
for a in input().split():
    B[int(a)] += 1
print(max(sum(B[i:i + 3])for i in range(10**5)))
