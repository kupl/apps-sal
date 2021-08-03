from collections import Counter as c
def read(): return list(map(int, input().split()))


n = int(input())
a = c(read())
print(a.most_common(1)[0][1])
