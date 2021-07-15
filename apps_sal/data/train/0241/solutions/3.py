class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
      # loop through all the commands in the arr
      # scenario the direction is not facing the same

        def is_infinite_loop(command):
            # iterate over all the commands 
            # direction 0: NameError
            # x and y coordinates, if x and 0 is (0, 0) return True
            direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            d_index = 0
            x, y = 0, 0
            for move in command:
                if move == 'G':
                    x += direction[d_index][0]
                    y += direction[d_index][1]
                elif move == 'R':
                    d_index = (d_index + 1) % 4
                elif move == 'L':
                    d_index = (d_index + 3) % 4
            # if back at origin
            # print(d_index)
            if x == y == 0:
                return True
            if (x != 0 or y != 0) and d_index != 0:
                return True
            return False

        return is_infinite_loop(instructions)

# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         L_occurances = instructions.count('L')
#         R_occurances = instructions.count('R')
#         difference = L_occurances - R_occurances
        
#         if difference % 4 == 0:
#             # check if loop otherwise return False too
#             directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W
#             d = 0                                           # start at North index
#             point = [0, 0]
#             for instruction in instructions:
#                 if instruction == 'G':
#                     point[0] += directions[d][0]
#                     point[1] += directions[d][1]
#                 elif instruction == 'L':
#                     d = (d + 3) % 4
#                 elif instruction == 'R':
#                     d = (d + 1) % 4
#             return True if point == [0, 0] else False
#         else:
#             return True
        
        
#         # return True if L_occurances - R_occurances != 0 else False

