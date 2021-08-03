A, B, C, D, E, F = (int(T) for T in input().split())
SugM = 0
WatM = 100 * A
for TC in range(0, F + 1):
    for TD in range(0, F + 1):
        Suger = C * TC + D * TD
        RestS = F - Suger
        if RestS >= 0:
            for TA in range(0, (RestS // 100) + 1):
                for TB in range(0, (RestS // 100) + 1):
                    if TA == TB == 0:
                        continue
                    else:
                        Water = TA * A * 100 + TB * B * 100
                        RestW = RestS - Water
                        if RestW >= 0 and Water >= (100 * Suger) / E:
                            if SugM / (WatM + SugM) < Suger / (Water + Suger):
                                SugM = Suger
                                WatM = Water
                        else:
                            break
        else:
            break
print('{} {}'.format(WatM + SugM, SugM))
