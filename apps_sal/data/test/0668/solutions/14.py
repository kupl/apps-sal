'''
def send_message(student):
	nonlocal data, last_student_that_knows, student_that_sends, number_of_messages, output
	for i in range(data[student]):
		if last_student_that_knows == amount_of_students - 1:
			break
		last_student_that_knows += 1
		number_of_messages += 1
		output.append("{0} {1}".format(student + 1, last_student_that_knows + 1))
		send_message(last_student_that_knows)
'''
############################################
amount_of_students = int(input())
data = input().split(" ")
students = []
for i in range(len(data)):
	data[i] = int(data[i])
	students.append(0)
students[0] = 1 #Поликарп знает
############################################

def max_unaware_student():
	nonlocal data, students, number_of_messages, output
	max = -1
	student = -1
	for i in range(len(data)):
		if data[i] > max and students[i] == 0: #если этот студент отправляет больше и он ещё не знает
			max = data[i]
			student = i
	return student

def send_message(student):
	nonlocal data, students, number_of_messages, output
	for i in range(data[student]):
		if min(students) == 1: #если незнающие кончились
			break
		number_of_messages += 1
		recipient = max_unaware_student()
		output.append("{0} {1}".format(student + 1, recipient + 1))
		students[recipient] = 1
		send_message(recipient)

output = []
number_of_messages = 0

send_message(0)

if min(students) == 0:
	print("-1")

else:
	print(number_of_messages)
	for i in output:
		print (i)


