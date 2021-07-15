class Solution:
    def subarrayBitwiseORs(self, A):
        nums, n, pre = set(), len(A), set()
        for a in A:
            pre = {a} | {num | a for num in pre}
            nums |= pre
        return len(nums)

# @param {Integer[]} a
# @return {Integer}
#def subarray_bitwise_o_rs(a)
    # Get subarrays
#    solutions = {}
#    iterating_array = a.clone
#    a.each do |m|
#        num = m
#        iterating_array.each do |m|
#            solutions[num] = 1
#            num |= m
#        end
#        solutions[num] = 1
#        iterating_array.shift
#    end
#    solutions.keys.length
#end

