N = int(input())
S = input()
count = 1
check = S[0]

for c in S:
    if c != check:
        count += 1
        check = c

print(count)
