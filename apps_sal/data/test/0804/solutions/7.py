s = input()
k = int(input())
if len(s) < k:
    print('impossible')
else:
    print(max(k - len(set([i for i in s])), 0))
