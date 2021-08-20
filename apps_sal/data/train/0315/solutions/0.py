class Solution:

    def minimumSwap(self, s1: str, s2: str) -> int:
        xy_pair = 0
        yx_pair = 0
        for (c1, c2) in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                xy_pair += 1
            elif c1 == 'y' and c2 == 'x':
                yx_pair += 1
        if (xy_pair + yx_pair) % 2 == 1:
            return -1
        return xy_pair // 2 + yx_pair // 2 + xy_pair % 2 + yx_pair % 2


'\n"xx"\n"yy"\n"xy"\n"yx"\n"xx"\n"xy"\n"xyxy"\n"yxyx"\n"xxyyxxyxyxyx"\n"xyxyxyxxyyxx"\n"xxyyxyxyxx"\n"xyyxyxxxyx"\n"xyxyxyyxx"\n"yxyyyxxxx"\n"xyxyxyyxxxyyxyxxxyx"\n"yxyyyxxxxxxyyxyxyxx"\n'
