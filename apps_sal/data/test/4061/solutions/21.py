def int_multiple():
    return  [int(c) for c in input().split()]

def int_single():
    return int(input())

def str_multiple():
    return [c for c in input().split()]

def str_single():
    return input()

# start

s = str_single()
t = str_single()


ti = 0

start = []
for si in range(len(s)):
    if(s[si] == t[ti]):
        start.append(si)
        ti += 1
        if ti == len(t):
            break

end = []
ti = len(t) - 1
for si in reversed(list(range(len(s)))):
    if (s[si] == t[ti]):
        end.append(si)
        ti -= 1
        if ti < 0:
            break

end = list(reversed(end))

start_mx = len(s) - start[-1] - 1
end_mx = end[0]
mx_between = 0
for i in range(len(t)-1):
    diff = end[i+1] - start[i] - 1
    mx_between = max(mx_between, diff)

print(max(start_mx, end_mx, mx_between))

