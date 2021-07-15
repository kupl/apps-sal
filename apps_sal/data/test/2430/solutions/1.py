class Task:
	h = []
	answer = 0
	
	def getData(self):
		h_size = int(input())
		self.h = [int(input()) for i in range(h_size)]
	
	def solve(self):
		current_level = 0
		for i in range (0, len(self.h)):
			self.answer += self.h[i] - current_level + 1
			if i == len(self.h) - 1:
				return
			if self.h[i + 1] < self.h[i]:
				self.answer += self.h[i] - self.h[i + 1]
				current_level = self.h[i + 1]
			else:
				current_level = self.h[i]
			self.answer += 1
	
	def printAnswer(self):
		print(self.answer)


task = Task();
task.getData();
task.solve();
task.printAnswer();

