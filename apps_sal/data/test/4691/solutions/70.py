def ans173(N: int, S: list):
    return (f"""AC x {(S.count("AC"))}
WA x {(S.count("WA"))}
TLE x {(S.count("TLE"))}
RE x {(S.count("RE"))}""")


N = int(input())
S = [input() for i in range(N)]
print(ans173(N, S))
