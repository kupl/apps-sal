def mp():
    return map(int, input().split())

n = int(input())
a = list(mp())
m = int(input())
b = list(mp())
print(max(a), max(b))
