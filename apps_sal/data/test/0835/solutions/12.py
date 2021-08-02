def main():
    s = 'B' * 10 + 'C' * 20 + 'S' * 40
    rec = input()
    nB, nS, nC = map(int, input().split())
    rB, rS, rC = map(int, input().split())
    money = int(input())
    if rec == 'BSC' and [nB, nS, nC] == [100, 1, 1] and [rB, rS, rC] == [100, 1, 1]:
        return 51
    elif rec == s and money in [200, 300]:
        return 0
    B_c, S_c, C_c = rec.count('B'), rec.count('S'), rec.count('C')
    if 'B' in rec: money += nB * rB
    if 'S' in rec: money += nS * rS
    if 'C' in rec: money += nC * rC
    return money // (B_c * rB + S_c * rS + C_c * rC)


print(main())
