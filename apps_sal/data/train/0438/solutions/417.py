class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == 1 and len(arr) == 1:
            return(1)
        if m > len(arr):
            return(-1)
        Bins = [0] * len(arr)
        Gs = {}
        Ge = {}
        Res = -1
        Rescnt = 0
        for y in range(len(arr)):
            i = arr[y] - 1
            if (i == 0 or Bins[i - 1] == 0) and (i == len(arr) - 1 or Bins[i + 1] == 0):
                Gs.update({i: 1})
                Ge.update({i: i})
                Bins[i] = 1
                if m == 1:
                    Res = y + 1
                    Rescnt = Rescnt + 1
            else:
                if (i == 0 or Bins[i - 1] == 0) and (i < len(arr) - 1 and Bins[i + 1] == 1):
                    Gs.update({i: Gs[i + 1] + 1})
                    Ge[Gs[i + 1] + i] = i
                    tmp = Gs.pop(i + 1)
                    Bins[i] = 1
                    if Gs[i] == m:
                        Res = y + 1
                        Rescnt = Rescnt + 1
                    else:
                        if tmp == m:
                            Rescnt -= 1
                else:
                    if (i > 0 and Bins[i - 1] == 1) and (i == len(arr) - 1 or Bins[i + 1] == 0):

                        ix = Ge[i - 1]
                        tmp = Gs[ix]
                        Gs[ix] = Gs[ix] + 1
                        tmpe = Ge.pop(i - 1)
                        Ge.update({i: ix})
                        Bins[i] = 1
                        if Gs[ix] == m:
                            Res = y + 1
                            Rescnt = Rescnt + 1
                        else:
                            if tmp == m:
                                Rescnt -= 1
                    else:
                        if (i > 0 and Bins[i - 1] == 1) and (i < len(arr) - 1 and Bins[i + 1] == 1):

                            ix = Ge[i - 1]
                            tmp0 = Gs[ix]
                            Gs[ix] = Gs[ix] + Gs[i + 1] + 1
                            tmp = Gs.pop(i + 1)
                            tmpe = Ge.pop(i - 1)
                            Ge[tmp + i] = ix
                            Bins[i] = 1
                            if Gs[ix] == m:
                                Res = y + 1
                                Rescnt = Rescnt + 1
                            else:
                                if tmp == m:
                                    Rescnt -= 1
                                if tmp0 == m:
                                    Rescnt -= 1
            if Rescnt > 0:
                Res = y + 1

        return(Res)
