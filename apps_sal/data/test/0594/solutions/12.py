
nums = input()
correct = input()
incorrect = input()

correct_times = [ int(i) for i in correct.split(' ') ]
incorrect_times = [ int(i) for i in incorrect.split(' ') ]

correct_times = sorted(correct_times)
incorrect_times = sorted(incorrect_times)

v = max([ 2 * correct_times[0], correct_times[-1] ])

if v >= incorrect_times[0]:
    print(-1)
else:
    print(v)

