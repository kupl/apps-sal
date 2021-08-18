def judge_kaibun(S):
    return S == S[::-1]


S = input()

if judge_kaibun(S):
    S_part1 = S[(len(S) + 1) // 2:]
    S_part2 = S[:(len(S) - 1) // 2]
    if judge_kaibun(S_part1) and judge_kaibun(S_part2):
        print("Yes")
    else:
        print("No")
else:
    print("No")
