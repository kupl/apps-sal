def ans173(N: int, S: list):
    return f"AC x {S.count('AC')}\nWA x {S.count('WA')}\nTLE x {S.count('TLE')}\nRE x {S.count('RE')}"


N = int(input())
S = [input() for i in range(N)]
print(ans173(N, S))
