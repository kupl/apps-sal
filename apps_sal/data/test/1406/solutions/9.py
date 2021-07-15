#http://codeforces.com/problemset/problem/459/C

# Input of the values
n, k, d = list(map(int, input().split()))

#Convention : 	Busses are numbered from 1 to k
#				Students are numbered from 0 to k - 1
# 				Days are numbered from 0 to k - 1

# Variable for success
success = True

# answer is a  2-d array that stores the bus number each student used on a particular day
# Students are numbered from 0 to n-1
answer = [[] for x in range(n)]

# Initialising the first students details manually
# The first student uses the bus 1 for all of the days
answer[0] = [1 for x in range(d)]

# we will be filling the details for each and every student and 
# would print -1 only if we cannot allot any bus number to the next student
for i_th_student in range(1,n):
	
	#answer for previous value
	i_minus_one_student = answer[i_th_student - 1]

	# Answer to the current student
	current_student = list(i_minus_one_student)

	# Days are also numbered from 0 to d-1
	for i_th_day in reversed(list(range(d))):

		# the condition to change the bus number 
		if i_minus_one_student[i_th_day] < k :

			current_student[i_th_day] += 1

			# all the numbers next to it are reset
			for i in range(i_th_day + 1, d):
				current_student[i] = 1
			
			break
	
	#Save the value
	answer[i_th_student] = current_student
	
	#Failed
	if current_student == i_minus_one_student:
		success = False
		break

# printing the output
if not(success):
	print ("-1")

else:
	# ans_trans is used for giving the output fast
	answer_trans= [[] for i in range(d)]
	for y in range(n):
		i = 0
		for x in answer[y]:
			answer_trans[i].append(x)
			i += 1
	for bla in answer_trans:
		print(' '.join(map(str, bla)))

