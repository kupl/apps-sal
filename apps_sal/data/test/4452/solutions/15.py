t = int(input())
for i in range(t):
    n = input()
    print(len(n) - n.count('0'))
    for j in range(len(n)):
        if n[j] != '0':
            print(n[j], '0' * (len(n) - j - 1),end=' ', sep='')
    print()
