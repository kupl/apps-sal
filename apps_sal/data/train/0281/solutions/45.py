class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if(len(s) != len(t)):
            return False
        idx_dict = [0] * 26

        for idx, sc in enumerate(s):
            tc = t[idx]

            if(sc == tc):
                continue

            sasc = ord(sc)
            tasc = ord(tc)

            if(sasc < tasc):
                movei = tasc - sasc
            else:
                movei = 26 - sasc + tasc
            origini = movei
            movei = movei + 26 * idx_dict[movei]
            idx_dict[origini] += 1
            if(movei > k):
                return False
        return True
