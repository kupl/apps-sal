polynum = int(input())
length = list(map(int, input().split()))
most_l = max(length)
othersum = sum(length) - most_l
if othersum > most_l:
    print('Yes')
else:
    print('No')
