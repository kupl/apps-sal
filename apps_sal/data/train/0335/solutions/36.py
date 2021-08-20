class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        sums_lookup = {}
        sums_lookup[0] = 0
        for rod in rods:
            newMembers = {}
            for key in sums_lookup.keys():
                value = sums_lookup[key]
                if rod + key not in newMembers:
                    newMembers[rod + key] = rod + value
                elif rod + value > newMembers[rod + key]:
                    newMembers[rod + key] = rod + value
                if key - rod not in newMembers:
                    newMembers[key - rod] = value
                elif value > newMembers[key - rod]:
                    newMembers[key - rod] = value
                if key not in newMembers:
                    newMembers[key] = value
                elif value > newMembers[key]:
                    newMembers[key] = value
            for key in newMembers.keys():
                sums_lookup[key] = newMembers[key]
        return sums_lookup[0]
