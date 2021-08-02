length, dna = int(input()), input()
nums = [dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')]
print((nums.count(max(nums))**length) % 1000000007)
