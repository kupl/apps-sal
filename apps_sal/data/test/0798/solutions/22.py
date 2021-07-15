def main(nums):
	t = nums[0]
	for i in range(0, t+1): #between 1->2
		q = nums[1] #must be at 2
		w = q-i #between 2->3
		e = t-i #between 1->3
		r = nums[2] #must be at 3
		f = w+e #for real at 3

		if r!=f or w<0:
			continue
		else:
			return '{} {} {}'.format(i, w, e)

	return 'Impossible'

def init():
	nums = list(map(int, input().split()))

	print(main(nums))

init()
