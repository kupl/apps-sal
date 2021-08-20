def dfs(li):
    if int(''.join(li)) > N:
        return 0
    ret = 1 if all((n in li for n in nums)) else 0
    for i in nums:
        ret += dfs(li + [i])
    return ret


N = int(input())
nums = ['3', '5', '7']
print(dfs(['0']))
