t = int(input())
for request in range(t):
    n, k = map(int, input().split())
    box = list(input())
    pattern = '()' * (k - 1) + '(' + ('()' * ((n - (k) * 2) // 2) ) + ')'
    changes = []
    for i in range(n):
        if box[i] != pattern[i]:
            for j in range(i + 1, n):
                if box[j] == pattern[i]:
                    for z in range((j - i + 1) // 2):
                        box[i + z], box[j - z] = box[j - z], box[i + z]
                    changes.append((i + 1, j + 1))
                    break
    print(len(changes))
    for i in range(len(changes)):
        print(*changes[i])
