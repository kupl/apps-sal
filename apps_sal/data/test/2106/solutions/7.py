# CF 241/A 1300

# S = supply in city i
# D = distance from c[i] to c[i + 1]
# k = refresh interval
# min time to arrive at C[n] where n = m + 1

def f(k, D, S):
    n = len(D)

    # travel time is at least the sum of all distances
    time = sum(D)

    fuel = 0
    best = 0

    for i in range(n):
        assert fuel >= 0
        # enter i-th city
        # fuel is either negative (we need extra) or zero
        # add S[i] fuel for free
        # subtract distance to city i+1
        fuel += (S[i] - D[i])
        if S[i] > S[best]:
            best = i
        if fuel < 0: # best station for i..lastpos
            need = -fuel
            count = need // S[best]
            if need % S[best] != 0:
                count += 1
            time += count * k
            fuel += S[best] * count

    return time

assert f(4, [15, 20, 14, 10, 39, 4, 26, 8, 8, 30, 13, 43, 7, 7, 4, 6, 23, 42, 24, 35, 12, 19, 21, 31, 5, 20, 8, 17, 25, 31, 8, 31, 9, 14, 29, 35, 39, 35, 19, 13, 35, 11, 24, 3, 22, 3, 22, 41, 26, 32, 17, 42, 21, 16, 15, 44, 12, 5, 16, 20, 19, 38, 15, 11, 36, 14, 6, 21, 5, 27, 15, 40, 6, 9, 32, 33, 35, 4, 10, 15, 26], [3, 5, 4, 3, 4, 6, 4, 7, 5, 4, 3, 4, 3, 3, 4, 3, 4, 3, 3, 4, 6, 5, 5, 3, 3, 6, 6, 5, 3, 3, 5, 3, 3, 6, 4, 4, 3, 6, 4, 3, 3, 5, 6, 6, 7, 3, 3, 3, 3, 3, 7, 3, 3, 5, 3, 3, 3, 4, 6, 4, 6, 4, 5, 3, 3, 6, 4, 3, 3, 3, 7, 5, 4, 5, 3, 5, 4, 3, 3, 4, 3]) == 2419

assert f(10, [4, 4, 4], [1, 2, 3]) == 3 * 10 + 1 * 10 + 10 + 12
assert f(10, [5], [5]) == 5
assert f(10, [6], [5]) == 16
assert f(20, [5, 5], [5, 5]) == 10
assert f(5,  [2, 2, 2], [1, 1, 1]) == 6 + 5 + 5 + 5
assert f(5,  [1, 1, 1], [3, 0, 0]) == 3
assert f(10, [4, 4, 4], [6, 5, 3]) == 12

assert f(6, [1, 2, 5, 2], [2, 3, 3, 4]) == 10
assert f(5, [10, 10, 10], [5, 10, 1]) == 40
assert f(3, [5, 6], [5, 5]) == 14
assert f(3, [11, 8, 8, 12, 17, 4, 4, 25, 39, 37, 31, 32, 38, 34, 29, 29, 34, 39, 39, 39, 17, 9, 24, 6], [3, 5, 4, 3, 3, 3, 4, 3, 4, 3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 3, 3, 3, 3, 3]) == 862


m, k = list(map(int, input().split()))
D = list(map(int, input().split()))
S = list(map(int, input().split()))
ans = f(k, D, S)
print(ans)

