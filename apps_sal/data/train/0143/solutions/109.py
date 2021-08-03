class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        insp = {}
        pos = {}
        mxx = -1
        i = 0
        while i < len(tree):
            f = tree[i]
            if f not in insp and len(insp) == 2:
                mnn = math.inf
                tod = None
                for of, op in list(pos.items()):
                    mnn = min(mnn, op)
                    if mnn == op:
                        tod = of
                k = pos[tod]
                while k >= 0:
                    of = tree[k]
                    if of not in pos:
                        break
                    insp[of] -= 1
                    k -= 1

                del pos[tod]
                del insp[tod]
                insp[f] = 0
            elif f not in insp:
                insp[f] = 0

            pos[f] = i
            insp[f] += 1
            score = self.get_basketsize(insp)
            mxx = max(mxx, score)
            i += 1

        return mxx

    def get_basketsize(self, insp):
        mxx = 0
        nmxx = 0
        for f, ct in list(insp.items()):
            if ct >= mxx:
                nmxx = max(mxx, nmxx)
                mxx = max(ct, mxx)
            elif ct >= nmxx:
                nmxx = max(ct, nmxx)
        return mxx + nmxx
