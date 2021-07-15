n = int(input())
level = input().strip()
for l in range(1, n + 1):
    for i in range(n - l + 1):
        for j in range(5):
            if i + l * j >= n or level[i + l * j] == '.':
                break
        else:
            print('yes')
            return
print('no')

