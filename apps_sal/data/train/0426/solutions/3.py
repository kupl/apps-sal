class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        all_powers_of_two_up_to_limit_sorted = [sorted(str(1 << i)) for i in range(30)]
        return sorted(str(N)) in all_powers_of_two_up_to_limit_sorted
