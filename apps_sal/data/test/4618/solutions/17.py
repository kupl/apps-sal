s = input()
K = int(input())

case = []
append = case.append
for i in range(1, K + 1):
    for idx in range(0, len(s) - (i - 1)):
        if s[idx:idx + i] not in case:
            append(s[idx:idx + i])
case.sort(reverse=True)

print(case[-K])
