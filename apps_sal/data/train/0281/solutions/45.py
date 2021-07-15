class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if(len(s) != len(t)):
            return False
        idx_dict = [0] * 26
        # for i in range(1, 26):
        #     idx_dict[i] = 0
        
        for idx, sc in enumerate(s):
            tc = t[idx]
            
            if(sc == tc):
                # idx_list.append(0)
                continue
            
            sasc = ord(sc)
            tasc = ord(tc)
            
            if(sasc < tasc):
                movei = tasc - sasc
            else:
                movei = 26 - sasc + tasc
            # while(movei in idx_set):
            #         movei = movei + 26
            origini = movei
            movei = movei + 26 * idx_dict[movei]
            idx_dict[origini] += 1
            if(movei > k):
                return False
            # idx_list.append(movei)
            # idx_set.add(movei)
        #print(idx_list)
        return True

