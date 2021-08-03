S = input()
count = 0

for i in range(len(S)):
    if S[i] == "+":
        count += 1
    else:
        count -= 1
print(count)
