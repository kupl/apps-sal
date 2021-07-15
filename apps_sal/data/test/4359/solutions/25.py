abcde = [int(input()) for _ in range(5)]

s = list(map(lambda x: (10-x%10)%10, abcde))
print(sum(abcde)+sum(s)-max(s))
