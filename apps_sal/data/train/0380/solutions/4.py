class Solution:

    def checkIPv4(self, IP):
        IP = IP.lower().split(".")
        if len(IP) != 4:
            return False
        for block in IP:
            try:
                k = int(block)
                if (not 0 <= k <= 255) or (k > 0 and block[0] == '0') or \
                   (k == 0 and len(block) > 1):
                    return False
            except ValueError:
                return False
        return True

    def checkIPv6(self, IP):
        IP = IP.lower().split(":")
        if len(IP) != 8:
            return False
        for block in IP:
            try:
                k = int("0x" + block, 16)
                if (len(block) > 4) or (not 0 <= k <= 65535):
                    return False
            except ValueError:
                return False
        return True

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.checkIPv4(IP):
            return "IPv4"
        elif self.checkIPv6(IP):
            return "IPv6"
        else:
            return "Neither"
