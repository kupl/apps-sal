
def register(diffs, index, a):
    if index not in diffs:
        diffs[index] = a
    else:
        diffs[index] = max(diffs[index], a)


def get_height(rods):
    diffs = {0: 0}
    for rod in rods:
        new_diffs = {}
        for diff, a in diffs.items():
            register(new_diffs, diff, a)
            register(new_diffs, diff + rod, a)
            register(new_diffs, diff - rod, a + rod)
        diffs = new_diffs

    return diffs[0]


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        return get_height(rods)
