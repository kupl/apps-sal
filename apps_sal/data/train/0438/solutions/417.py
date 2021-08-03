class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == 1 and len(arr) == 1:
            return(1)
        if m > len(arr):
            return(-1)
        Bins = [0] * len(arr)
        Gs = {}  # start,len
        Ge = {}  # end,start ix
        Res = -1
        Rescnt = 0
        for y in range(len(arr)):
            i = arr[y] - 1
            if (i == 0 or Bins[i - 1] == 0) and (i == len(arr) - 1 or Bins[i + 1] == 0):
                # new group
                # Gl[i]=1
                # Gs[i]=i
                Gs.update({i: 1})
                Ge.update({i: i})
                Bins[i] = 1
                # ix=len(Gs)-1
                if m == 1:
                    Res = y + 1
                    Rescnt = Rescnt + 1
                    # print(Res,Rescnt)
            else:
                if (i == 0 or Bins[i - 1] == 0) and (i < len(arr) - 1 and Bins[i + 1] == 1):
                    # extend left i+1
                    # ix=[k for k,j in enumerate(Gs) if j[0]==(i+1)][0]
                    Gs.update({i: Gs[i + 1] + 1})
                    Ge[Gs[i + 1] + i] = i
                    tmp = Gs.pop(i + 1)
                    # tmpe=Ge.pop(i+1)
                    Bins[i] = 1
                    if Gs[i] == m:
                        Res = y + 1
                        Rescnt = Rescnt + 1
                    else:
                        if tmp == m:
                            Rescnt -= 1
                else:
                    if (i > 0 and Bins[i - 1] == 1) and (i == len(arr) - 1 or Bins[i + 1] == 0):
                        # extend right i-1
                        # strt=i-1
                        # while(strt>0 and Bins[strt]==1):strt-=1
                        # if(Bins[strt]==0):strt+=1

                        # ix=[k for k in Gs.keys() if k+Gs[k]==i][0]
                        # ix=[k for k,j in enumerate(Gs) if j[0]==strt][0]
                        ix = Ge[i - 1]
                        tmp = Gs[ix]
                        Gs[ix] = Gs[ix] + 1
                        tmpe = Ge.pop(i - 1)
                        Ge.update({i: ix})
                        Bins[i] = 1
                        # if(Gs[ix][1]==m):Res=i
                        if Gs[ix] == m:
                            Res = y + 1
                            Rescnt = Rescnt + 1
                        else:
                            if tmp == m:
                                Rescnt -= 1
                    else:
                        if (i > 0 and Bins[i - 1] == 1) and (i < len(arr) - 1 and Bins[i + 1] == 1):
                            # merge Len=Sum+1

                            # ix=[k for k in Gs.keys() if k+Gs[k]==i][0]
                            # print('merge',i)
                            ix = Ge[i - 1]
                            # print('ix',ix,i)
                            tmp0 = Gs[ix]
                            Gs[ix] = Gs[ix] + Gs[i + 1] + 1
                            tmp = Gs.pop(i + 1)
                            tmpe = Ge.pop(i - 1)
                            # print('ix2',tmp+i)
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
            # print(i,'E',Ge)
            # print('S',Gs)

            # for r in range(len(Gs)):
            #         if Gs[r][1]==m:
            #             Res=y+1
            #             break
        return(Res)
