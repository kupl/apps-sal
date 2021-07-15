def read_data():
    n = int(input())
    Ls = list(map(int, input().split()))
    Ds = list(map(int, input().split()))
    return n, Ls, Ds

def solve(n, Ls, Ds):
    freqD = [0] * 201
    for d in Ds:
        freqD[d] += 1
    LDs = list(zip(Ls, Ds))
    LDs.sort(reverse = True)
    prevL = 0
    ni = 0
    record = float('inf')
    cost_long = 0
    cost_me = 0
    for L, D in LDs:
        if prevL != L:
            n -= ni
            record = min(record, cost_long + calc_cost(ni, n, freqD))
            prevL = L
            ni = 0
            cost_long += cost_me
            if cost_long >= record:
                return record
            cost_me = 0
        freqD[D] -= 1
        cost_me += D
        ni += 1
    record = min(record, cost_long)
    return record

def calc_cost(ni, n, freqD):
    if n < ni:
        return 0
    cost = 0
    for d, f in enumerate(freqD):
        if n - f >= ni:
            cost += f * d
            n -= f
        else:
            cost += (n - ni + 1) * d
            return cost
    return float('inf')

n, Ls, Ds = read_data()
print(solve(n, Ls, Ds))
