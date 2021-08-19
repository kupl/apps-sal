abc = list(map(int, input().split()))
abc.sort()
print('Yes' if abc[0] + abc[1] == abc[2] else 'No')
