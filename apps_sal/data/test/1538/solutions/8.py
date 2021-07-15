def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())
from collections import Counter

n = ii()
a = li()
x = Counter(a).most_common(1)[0][1]
print(x)
