abc = list(map(str, input().split()))
abc.sort()
print(int(abc[2] + abc[1]) + int(abc[0]))
