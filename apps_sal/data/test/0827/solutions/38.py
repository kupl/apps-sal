N = int(input())
T = str(input())

mozi = "110" * (N//3+2)
count = 0

for i in range(3):
    if mozi[i:i+len(T)] == T:
        count += 1
if count == 0:
    result = 0
elif T == "1":
    result = 10 ** 10
    result *= 2
elif T == "11":
    result = 10**10
else:
    K = 0
    for t in T:
        if t == "0":
            K += 1
    if T[-1] == "0":
        result = 10**10-K+1
    else:
        result = 10**10-K

print(result)
