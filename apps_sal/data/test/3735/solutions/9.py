n = int(input())

def get(a):
    return sum(map(int, str(a)))

def solve(n):
    cnt = len(str(n))
    if cnt == 1:
        return get(n)
    ret = get(n)
    for a in ['9' * (cnt - 1)]:
        ret = max(get(int(a)) + get(n - int(a)), ret)
    return ret
    
print(solve(n))


